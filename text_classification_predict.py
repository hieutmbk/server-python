import pandas as pd


from sklearn.model_selection import train_test_split
import os

from sklearn.externals import joblib
from feature_transformer import FeatureTransformer
from sklearn.pipeline import Pipeline

pkl_filename = 'svm_model.sav'
filename_countvect = 'finalized_countvectorizer.sav'
filename_tfidf = 'finalized_tfidftransformer.sav'

class TextClassificationPredict(object):
    def __init__(self):
        self.test = None

    # def train_data(self):
    #     # Tạo train data
    #     dataset = []
    #
    #     for files in os.walk("data"):
    #         feature = []
    #         target = []
    #         for file in files[2]:
    #             file_name = "data/"+file
    #             name_target = file[0:file.index(".")]
    #             with open(file_name,encoding="UTF-8") as f:
    #                 for line in f.readlines():
    #
    #                     feature.append(line)
    #                     target.append(name_target)
    #         dataset.append(feature)
    #         dataset.append(target)
    #
    #
    #     df_data = pd.DataFrame(dataset)
    #     X = df_data.iloc[0]
    #
    #     Y = df_data.iloc[1]
    #
    #     X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=1)
    #
    #     # init models
    #     model  = SVMModel()
    #
    #     clf = model.clf.fit(X_train, y_train)
    #
    #     score = clf.score(X_test, y_test, sample_weight=None)
    #
    #     print(score)
    #
    #
    #     joblib.dump(clf.named_steps.get("clf-svm"), pkl_filename)
    #
    #
    #     joblib.dump(clf.named_steps.get("vect"), filename_countvect)
    #
    #     joblib.dump(clf.named_steps.get("tfidf"), filename_tfidf)
    #     print("Dump success")

    def check_file_exist(self,filename):
        return os.path.exists(filename)

    def predict(self):
        if self.check_file_exist(pkl_filename) is False :
            print("Model is not exist")
            self.train_data()
        else:

            clf_svm = joblib.load(pkl_filename)
            loaded_cvec = joblib.load(filename_countvect)
            loaded_tfidf_transformer = joblib.load(filename_tfidf)
            pipe_line = Pipeline([
                ("transformer", FeatureTransformer()),
                ("vect", loaded_cvec),
                ("tfidf", loaded_tfidf_transformer),
                ("clf-svm", clf_svm)
            ])
            print(pipe_line.predict(["chỉnh điều hòa lên 25 độ"])[0])

if __name__ == '__main__':
    tcp = TextClassificationPredict()
    tcp.predict()
