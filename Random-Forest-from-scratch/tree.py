import numpy as np

#### Creating a decision tree ###
from collections import Counter
from sklearn.metrics import confusion_matrix, f1_score, precision_score, accuracy_score


class Node:
    """Class that represent the tree node"""

    def __init__(
        self, features=None, thresholds=None, left=None, right=None, value=None
    ):
        self.features = features
        self.thresholds = thresholds
        self.left = left
        self.right = right
        self.value = value


class DecisionTreeClassifier:
    def __init__(self, max_depth=100, min_samples_split=2):
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.root = None

    def _calculate_entropy(self, y):
        """Calculate the entropy from a group of labels"""
        counter = np.bincount(y)
        prob = counter / len(y)
        entropy = -np.sum([p * np.log2(p) for p in prob if p > 0])
        return entropy

    def _best_split(self, X, y):
        """Find the best split to increase the gain"""
        best_gain = -1
        best_feature = None
        best_threshold = None

        n_features = X.shape[1]

        for feature in range(n_features):
            thresholds = np.unique(X[:, feature])

            for threshold in thresholds:
                gain = self._information_gain(X, y, feature, threshold)

                if gain > best_gain:
                    best_gain = gain
                    best_feature = feature
                    best_threshold = threshold

        return best_feature, best_threshold

    def _grow_tree(self, X, y, depth=0):
        """Build recursively the tree"""
        # Stop Conditions
        n_samples = len(y)
        if (
            depth >= self.max_depth
            or n_samples < self.min_samples_split
            or len(np.unique(y)) == 1
        ):

            return self._leaf_node(y)

        feature, threshold = self._best_split(X, y)
        if feature is None:
            return self._leaf_node(y)

        left_idx = X[:, feature] <= threshold
        right_idx = X[:, feature] > threshold

        left = self._grow_tree(X[left_idx], y[left_idx], depth + 1)
        right = self._grow_tree(X[right_idx], y[right_idx], depth + 1)

        return Node(features=feature, thresholds=threshold, left=left, right=right)

    def fit(self, X, y):
        """Train the tree with the data"""
        self.root = self._grow_tree(X, y)

    def _predict_sample(self, x, node):
        """Predict the class of a sample"""
        if node.value is not None:
            return node.value

        if x[node.features] <= node.thresholds:
            return self._predict_sample(x, node.left)
        else:
            return self._predict_sample(x, node.right)

    def predict(self, X):
        """Predict multiple samples"""
        return np.array([self._predict_sample(x, self.root) for x in X])

    def _information_gain(self, X, y, feature, threshold):
        """Calculate information gain for a split"""
        left_idx = X[:, feature] <= threshold
        right_idx = X[:, feature] > threshold

        if np.sum(left_idx) == 0 or np.sum(right_idx) == 0:
            return 0

        parent_entropy = self._calculate_entropy(y)
        left_entropy = self._calculate_entropy(y[left_idx])
        right_entropy = self._calculate_entropy(y[right_idx])

        n_left = len(y[left_idx])
        n_right = len(y[right_idx])
        n_total = len(y)

        gain = parent_entropy - (
            (n_left / n_total) * left_entropy + (n_right / n_total) * right_entropy
        )
        return gain

    def _leaf_node(self, y):
        """Create a leaf node with the most common class"""
        value = Counter(y).most_common(1)[0][0]
        return Node(value=value)

    def metrics(self, y_true, y_pred):
        acc = accuracy_score(y_true, y_pred)
        f1 = f1_score(y_true, y_pred)
        precision = precision_score(y_true, y_pred)
        confusion = confusion_matrix(y_true, y_pred)

        print(f"Accuracy: {acc*100:.2f}%")
        print(f"Precision: {precision*100:.2f}%")
        print(f"F1 score: {f1:.4f}")
        print("Confusion Matrix:\n", confusion)
