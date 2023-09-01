#!/usr/bin/env python3
"""Test for the ee.computedobject module."""

import ee
from ee import apitestcase
import unittest


class ComputedObjectTest(apitestcase.ApiTestCase):

  def testComputedObject(self):
    """Verifies that untyped calls wrap the result in a ComputedObject."""

    result = ee.ApiFunction.call_('DateRange', 1, 2)
    self.assertIsInstance(result.serialize(), str)
    self.assertEqual({'value': 'fakeValue'}, result.getInfo())

  def testInternals(self):
    """Test eq(), ne() and hash()."""
    a = ee.ApiFunction.call_('DateRange', 1, 2)
    b = ee.ApiFunction.call_('DateRange', 2, 3)
    c = ee.ApiFunction.call_('DateRange', 1, 2)

    self.assertEqual(a, a)
    self.assertNotEqual(a, b)
    self.assertEqual(a, c)
    self.assertNotEqual(b, c)
    self.assertNotEqual(hash(a), hash(b))


if __name__ == '__main__':
  unittest.main()
