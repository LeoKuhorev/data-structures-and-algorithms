import pytest
from challenges.eeney_meeney_miney_moe.eeney_meeney_miney_moe import eeney_meeney_miney_moe as emmm


class TestEMMM:

    def test_emmm_happy_path(self):
        names = ['A', 'B', 'C', 'D', 'E']
        k = 3
        assert emmm(names, 3) == 'D'
