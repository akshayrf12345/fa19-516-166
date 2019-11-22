from __future__ import print_function
from cloudmesh.shell.command import command
from cloudmesh.shell.command import PluginCommand
from cloudmesh.frugal.api.manager import Manager
from cloudmesh.common.console import Console
from cloudmesh.common.util import path_expand
from pprint import pprint
from cloudmesh.common.debug import VERBOSE
import pandas as pd
import numpy as np
from cloudmesh.common.Printer import Printer
from cloudmesh.frugal.api import helpers

class FrugalCommand(PluginCommand):

    # noinspection PyUnusedLocal
    @command
    def do_frugal(self, args, arguments):
        """
        ::

          Usage:
                frugal list --refresh=REFRESH --order=ORDER --resultssize=RESULTSSIZE
                frugal list --refresh=REFRESH --order=ORDER
                frugal list --order=ORDER --resultssize=RESULTSSIZE
                frugal list --refresh=REFRESH --resultssize=RESULTSSIZE
                frugal list --resultssize=RESULTSSIZE
                frugal list --order=ORDER
                frugal list --refresh=REFRESH
                frugal list
                frugal boot --refresh=REFRESH --order=ORDER
                frugal boot --order=ORDER
                frugal boot --refresh=REFRESH
                frugal boot

          This command does some useful things.

          Arguments:
              REFRESH forces a refresh on the flavors across GCP, AWS, and Azure
              ORDER Either ['price' (default), 'cores', 'memory')

          Options:
              -order      order by memory, cores, or price
              -refresh    force refresh

        """
        arguments.REFRESH = arguments['--refresh'] or None
        arguments.RESULTSSIZE = arguments['--resultssize'] or None
        arguments.ORDER = arguments['--order'] or None

        #VERBOSE(arguments)

        m = Manager()

        if arguments.ORDER is None:
            arguments.ORDER='price'

        if arguments.REFRESH is None:
            arguments.REFRESH=False

        if arguments.RESULTSSIZE is None:
            arguments.RESULTSSIZE=25


        if arguments.list:
            m.list(order = arguments.ORDER,refresh =bool(arguments.REFRESH == 'True'), resultssize= int(arguments.RESULTSSIZE))

        if arguments.boot:
            m.boot(order = arguments.ORDER,refresh =bool(arguments.REFRESH == 'True'))

        return ""
