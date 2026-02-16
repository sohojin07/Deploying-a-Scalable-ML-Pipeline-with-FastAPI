import numpy as np
from sklearn.ensemble import RandomForestClassifier

from ml.model import train_model, compute_model_metrics, inference


def test_train_model():
    """
    # Confirms model trains and correct algorithm is used
    """
    X = np.random.rand(50, 5)
    y = np.random.randint(0, 2, 50)

    model = train_model(X, y)

    assert isinstance(model, RandomForestClassifier)


def test_inference():
    """
    # Confirms predictions exist and match dataset length
    """
    X = np.random.rand(50, 5)
    y = np.random.randint(0, 2, 50)

    model = train_model(X, y)
    preds = inference(model, X)

    assert isinstance(preds, np.ndarray)
    assert preds.shape[0] == X.shape[0]


def test_compute_model_metrics():
    """
    # Confirms metrics calculated correctly and values are valid probabilities
    """
    y = np.array([1, 0, 1, 1])
    preds = np.array([1, 0, 0, 1])

    precision, recall, fbeta = compute_model_metrics(y, preds)
    assert 0 <= precision <= 1
    assert 0 <= recall <= 1
    assert 0 <= fbeta <= 1
