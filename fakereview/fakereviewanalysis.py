import os
import numpy as np
import pandas as pd
from sklearn import model_selection
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

from fakereview import constants


def isTruthFullComment(comment):

    neg_deceptive_folder_path = constants.DATASET_PATH+str('negative_polarity\\deceptive_from_MTurk\\')
    neg_true_folder_path = constants.DATASET_PATH+str('negative_polarity\\truthful_from_Web\\')
    pos_deceptive_folder_path = constants.DATASET_PATH+str('positive_polarity\\deceptive_from_MTurk\\')
    pos_true_folder_path = constants.DATASET_PATH+str('positive_polarity\\truthful_from_TripAdvisor\\')

    #=================================================================================================
    polarity_class = []
    reviews = []
    spamity_class = []

    # =================================================================================================

    for i in range(1, 6):

        insideptru = pos_true_folder_path + 'fold' + str(i)
        insidepdec = pos_deceptive_folder_path + 'fold' + str(i)
        insidentru = neg_true_folder_path + 'fold' + str(i)
        insidendec = neg_deceptive_folder_path + 'fold' + str(i)

        for data_file in sorted(os.listdir(insidendec)):
            polarity_class.append('negtive')
            spamity_class.append(str(data_file.split('_')[0]))
            with open(os.path.join(insidendec, data_file)) as f:
                contents = f.read()
                reviews.append(contents)
        for data_file in sorted(os.listdir(insidentru)):
            polarity_class.append('negative')
            spamity_class.append(str(data_file.split('_')[0]))
            with open(os.path.join(insidentru, data_file)) as f:
                contents = f.read()
                reviews.append(contents)
        for data_file in sorted(os.listdir(insidepdec)):
            polarity_class.append('positive')
            spamity_class.append(str(data_file.split('_')[0]))
            with open(os.path.join(insidepdec, data_file)) as f:
                contents = f.read()
                reviews.append(contents)
        for data_file in sorted(os.listdir(insideptru)):
            polarity_class.append('positive')
            spamity_class.append(str(data_file.split('_')[0]))
            with open(os.path.join(insideptru, data_file)) as f:
                contents = f.read()
                reviews.append(contents)

    # =================================================================================================

    data_fm = pd.DataFrame({'polarity_class': polarity_class, 'review': reviews, 'spamity_class': spamity_class})

    data_fm.loc[data_fm['spamity_class'] == 'd', 'spamity_class'] = 0
    data_fm.loc[data_fm['spamity_class'] == 't', 'spamity_class'] = 1

    # =================================================================================================

    data_x = data_fm['review']

    data_y = np.asarray(data_fm['spamity_class'], dtype=int)

    X_train, X_test, y_train, y_test = model_selection.train_test_split(data_x, data_y, test_size=0.3)

    # =================================================================================================

    X_test = pd.Series([comment])

    cv = CountVectorizer()

    X_traincv = cv.fit_transform(X_train)
    X_testcv = cv.transform(X_test)

    # =================================================================================================

    nbayes = MultinomialNB()
    nbayes.fit(X_traincv, y_train)

    # =================================================================================================

    y_predictions = nbayes.predict(X_testcv)
    print("y predictions:",y_predictions)
    y_result = list(y_predictions)
    print("y result:", y_result)
    yp = ["Truthfull" if a == 1 else "Deceptive" for a in y_result]
    return yp[0]