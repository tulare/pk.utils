# -*- encoding: utf-8 -*-
from __future__ import (
    absolute_import,
    print_function, division,
    unicode_literals
)

__all__ = [ 'Requirements' ]

import sys
import os
import inspect

from pkg_resources import (
    DistributionNotFound,
    Requirement, Environment,
    require, get_distribution,
    working_set
)

from . import dialogs

class Requirements(object) :

    def __init__(self) :
        self._caller = ''
        self._requirements = []
        self._missing_distribs = []
        self._catalog = ''
        
        stack = list(
            filter(
                lambda s :
                    inspect.getframeinfo(s[0]).code_context is not None
                    and inspect.getframeinfo(s[0]).function == '<module>', 
                inspect.stack()
            )
        )

        try :
            self._caller = os.path.realpath(
                inspect.getfile(stack[-1][0])
            )
        except IndexError as e :
            pass

        self._req_file = self.caller.replace('.py', '.req')

        try :
            with open(self.req_file) as fp :
                self._requirements = [ Requirement.parse(req) for req in fp.readlines() ]  
        except FileNotFoundError as e :
            pass

    @property
    def catalog(self) :
        return self._catalog

    @catalog.setter
    def catalog(self, catalog) :
        self._catalog = catalog
            
    @property
    def caller(self) :
        return self._caller

    @property
    def req_file(self) :
        return self._req_file

    @property
    def requirements(self) :
        return self._requirements

    @property
    def missing_distribs(self) :
        return self._missing_distribs

    def add_requirement(self, requirement) :
        self._requirements.append(Requirement.parse(requirement))

    def satisfy(self) :
        environment = Environment([])
        self._missing_distribs = []

        for requirement in self.requirements :
            try :
                # distrib disponible directement ?
                distrib = get_distribution(requirement)
                environment.add(distrib)

            except DistributionNotFound as e :
                # meilleur candidat pour cette distrib aux emplacements suivants
                environment.scan([
                    os.path.dirname(self.caller) + '/eggs',
                    self.catalog + '/' + requirement.name
                ])
                distrib = environment.best_match(
                    requirement,
                    working_set
                )
                if distrib is not None :
                    working_set.add(distrib)
                else :
                    self._missing_distribs.append(requirement)

        if len(self.missing_distribs) > 0 :
            dialogs.error(
                list(map(str, self.missing_distribs)),
                'Missing distributions'
            )
            return False

        return True

        
