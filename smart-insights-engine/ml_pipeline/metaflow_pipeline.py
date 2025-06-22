from metaflow import FlowSpec, step

class TicketClassifierFlow(FlowSpec):

    @step
    def start(self):
        import pandas as pd
        self.data = pd.read_json("test_data/tickets.json")
        self.next(self.train)

    @step
    def train(self):
        from sklearn.feature_extraction.text import TfidfVectorizer
        from sklearn.linear_model import LogisticRegression
        X = TfidfVectorizer().fit_transform(self.data["text"])
        y = self.data["label"]
        self.model = LogisticRegression().fit(X, y)
        self.next(self.end)

    @step
    def end(self):
        import joblib
        joblib.dump(self.model, "model/classifier.pkl")

if __name__ == '__main__':
    TicketClassifierFlow()
