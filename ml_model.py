from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import ta

def train_model(df):
    df['MACD'] = ta.trend.macd(df['Close'])
    df['Target'] = (df['Close'].shift(-1) > df['Close']).astype(int)
    df.dropna(inplace=True)

    if len(df) < 10:  # Not enough data to train
        print("Not enough data for ML model.")
        return None, None

    X = df[['RSI', 'MACD', 'Volume']]
    y = df['Target']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, shuffle=False
    )
    model = LogisticRegression().fit(X_train, y_train)
    accuracy = accuracy_score(y_test, model.predict(X_test))
    return model, accuracy

