##########################################################################
#
#  Copyright (c) 2016, Image Engine Design Inc. All rights reserved.
#
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are
#  met:
#
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#
#     * Neither the name of Image Engine Design nor the names of any
#       other contributors to this software may be used to endorse or
#       promote products derived from this software without specific prior
#       written permission.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
#  IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
#  THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
#  PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
#  CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
#  EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
#  PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
#  PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
#  LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
#  NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
#  SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
##########################################################################

import unittest

import arnold

import IECore
import IECoreArnold

class SphereAlgoTest( unittest.TestCase ) :

	def testConvert( self ) :

		s = IECore.SpherePrimitive( 0.25 )
		with IECoreArnold.UniverseBlock() :

			n = IECoreArnold.NodeAlgo.convert( s )
			self.assertEqual( arnold.AiNodeEntryGetName( arnold.AiNodeGetNodeEntry( n ) ), "sphere" )
			self.assertEqual( arnold.AiNodeGetFlt( n, "radius" ), 0.25 )

	def testConvertWithMotion( self ) :

		s = [ IECore.SpherePrimitive( 0.25 ), IECore.SpherePrimitive( 0.5 ) ]

		with IECoreArnold.UniverseBlock() :

			n = IECoreArnold.NodeAlgo.convert( s, [ 0, 1 ] )
			self.assertEqual( arnold.AiNodeEntryGetName( arnold.AiNodeGetNodeEntry( n ) ), "sphere" )

			a = arnold.AiNodeGetArray( n, "radius" )
			self.assertEqual( arnold.AiArrayGetFlt( a, 0 ), 0.25 )
			self.assertEqual( arnold.AiArrayGetFlt( a, 1 ), 0.5 )

			a = arnold.AiNodeGetArray( n, "deform_time_samples" )
			self.assertEqual( arnold.AiArrayGetFlt( a, 0 ), 0 )
			self.assertEqual( arnold.AiArrayGetFlt( a, 1 ), 1 )

if __name__ == "__main__":
    unittest.main()
