#! /usr/bin/env python

#    SITools2 client for Python
#    Copyright (C) 2013 - Institut d'astrophysique spatiale
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses
import unittest
from sitools2.clients.gaia_client_medoc import *
from datetime import datetime, timedelta
from sitools2.clients import constants
__author__ = "Pablo ALINGERY, Jean-Christophe Malapert "
__date__ = "$9 juin 2013 12:17:18$"


sitools2_url = constants.SITOOLS2_URL
functional_test = constants.FUNCTIONAL_TEST


@unittest.skipUnless(functional_test, 'Functional test gaia-dem interface skipped')
class TestGaia(unittest.TestCase):
    def setUp(self):
        pass
    
    def testSearchGaia(self):
        print("\n####Test " + sitools2_url + " gaia_search() #############################")
        d1 = datetime(2012, 8, 10, 0, 0, 0)
        d2 = d1 + timedelta(days=1)
        gaia_data_list = gaia_search(DATES=[d1, d2], NB_RES_MAX=10)
        try:
            gaia_get(gaia_list=gaia_data_list, target_dir='results')
        except Exception:
            raise ValueError("Error Test gaia_get()")


if __name__ == "__main__":
    unittest.main()
