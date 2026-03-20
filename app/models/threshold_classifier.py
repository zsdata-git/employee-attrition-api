from sklearn.base import BaseEstimator, ClassifierMixin


class ThresholdClassifier(BaseEstimator, ClassifierMixin):
    def __init__(self, model, threshold=0.5):
        self.model = model
        self.threshold = threshold

    def fit(self, x, y=None):
        return self

    def predict_proba(self, x):
        return self.model.predict_proba(x)

    def predict(self, x):
        proba = self.predict_proba(x)[:, 1]
        return (proba >= self.threshold).astype(int)