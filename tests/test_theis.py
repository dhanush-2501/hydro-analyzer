import pytest
import numpy as np
from HyAn.solution.theis import Theis

@pytest.fixture
def theis():
    # data for the object
    time = [3, 5, 8, 12, 20, 24, 30, 38, 47, 50, 60, 70, 80, 90, 100, 130, 160, 200, 260, 320, 380, 500]
    drawdown = [0.3, 0.7, 1.3, 2.1, 3.2, 3.6, 4.1, 4.7, 5.1, 5.3, 5.7, 6.1, 6.3, 6.7, 7.0, 7.5, 8.3, 8.5, 9.2, 9.7, 10.2, 10.9]
    Q = 220
    r = 40

    return Theis(time=time, drawdown=drawdown, Q=Q, r=r)
# testing function fit
def test_fit(theis):
    data = [6.8809681705705845, 0.06650093540451595, [0.35080798514937, 0.82982904257002, 1.477368303627768, 2.1715234822178213, 3.182125911220257, 3.570887485511112, 4.062324541920257, 4.598569361407515, 5.092030719674994, 5.237390196641759, 5.669614917567605, 6.039084539851091, 6.361707826764922, 6.648026170606127, 6.905383319850745, 7.550595073349706, 8.064889222229484, 8.62046494584207, 9.276738267609034, 9.797983542250343, 10.230390867581551, 10.922448170770814]]
    res = theis.fit()
    assert res[0] == data[0]
    assert res[1] == data[1]
    assert np.array_equal(res[2], data[2])





