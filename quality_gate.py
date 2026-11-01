import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def main():
    rng = np.random.default_rng(42)

    X = rng.integers(0, 101, size=(200, 4))

    score = (
        0.40 * X[:, 0]
        + 0.25 * X[:, 1]
        + 0.20 * X[:, 2]
        + 0.15 * X[:, 3]
    )

    y = (score >= 50).astype(int)

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y
    )

    model = joblib.load("student_result_model.pkl")

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)

    threshold = 0.80

    print(f"Model accuracy: {accuracy:.4f}")
    print(f"Required accuracy: {threshold:.4f}")

    if accuracy < threshold:
        print("QUALITY GATE FAILED")
        raise SystemExit(1)

    print("QUALITY GATE PASSED")


if __name__ == "__main__":
    main()
