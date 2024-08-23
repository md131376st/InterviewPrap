import pytest
from .simpleConsept import Sample, SampleChild


class TestSimple:
    def test_print(self):
        sample1 = Sample()
        assert (0) == (sample1.get_var())
