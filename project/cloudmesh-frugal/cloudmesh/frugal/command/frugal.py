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
                frugal list --refresh=REFRESH --resultssize=RESULTSSIZE
                frugal list --refresh=REFRESH --order=ORDER --resultssize=RESULTSSIZE
                frugal list --resultssize=RESULTSSIZE
                frugal list --order=ORDER
                frugal list --refresh=REFRESH
                frugal list

          This command does some useful things.

          Arguments:
              REFRESH boolean
              ORDER boolean

          Options:
              -order      order by memory, cores, or price
              -refresh     force refresh

        """
        print(arguments)

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
            m.list(order = arguments.ORDER,refresh =bool(arguments.REFRESH), resultssize= int(arguments.RESULTSSIZE))

        Console.error("COMPLETE")
        return ""
