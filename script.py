from spam_data import training_spam_docs, training_doc_tokens, training_labels
from sklearn.naive_bayes import MultinomialNB
from preprocessing import preprocess_text

# Add your email text to test_text between the triple quotes:
test_text = """
Dear Customer,
Greetings from Flipkart!
We've created a new Flipkart account for you. A Flipkart account gives you a personalized shopping experience.
Your account details are:
Email for login: pratikk@gmail.com
Activation link: https://www.flipkart.com/account/guestaccountsignup?v1=J1KiIAZGoSWtMd2OLHbKIrJ1jlvUzLefnKAfjn8f/1pH0=
Flipkart Account benefits:
? Enjoy a faster checkout
? Track / Cancel / Return orders online
? Print / email invoices
? Add items to your wishlist and share them with friends and family
? Save your contact details so that you don\'t have to retype every time you order
? And more...
"""
test_tokens = preprocess_text(test_text)

def create_features_dictionary(document_tokens):
  features_dictionary = {}
  index = 0
  for token in document_tokens:
    if token not in features_dictionary:
      features_dictionary[token] = index
      index += 1
  return features_dictionary

def tokens_to_bow_vector(document_tokens, features_dictionary):
  bow_vector = [0] * len(features_dictionary)
  for token in document_tokens:
    if token in features_dictionary:
      feature_index = features_dictionary[token]
      bow_vector[feature_index] += 1
  return bow_vector

bow_sms_dictionary = create_features_dictionary(training_doc_tokens)
training_vectors = [tokens_to_bow_vector(training_doc, bow_sms_dictionary) for training_doc in training_spam_docs]
test_vectors = [tokens_to_bow_vector(test_tokens, bow_sms_dictionary)]

spam_classifier = MultinomialNB()
spam_classifier.fit(training_vectors, training_labels)

predictions = spam_classifier.predict(test_vectors)

print("Looks like a normal email!" if predictions[0] == 0 else "You've got spam!")