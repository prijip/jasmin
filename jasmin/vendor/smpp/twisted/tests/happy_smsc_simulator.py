"""
Copyright 2009-2010 Mozes, Inc.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either expressed or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""
import logging, struct, StringIO, binascii
from twisted.internet.protocol import Protocol, Factory
from twisted.internet import reactor, protocol
from jasmin.vendor.smpp.pdu.operations import *
from jasmin.vendor.smpp.pdu.pdu_encoding import PDUEncoder
from jasmin.vendor.smpp.pdu.pdu_types import *
from smsc_simulator import *

LOG_CATEGORY="smpp.twisted.tests.smsc_simulator"


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    factory          = Factory()
    factory.protocol = HappySMSC
    reactor.listenTCP(8007, factory)
    reactor.run()
