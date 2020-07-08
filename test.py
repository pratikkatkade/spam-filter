load_file_in_context("script.py")

try:
  if most_common_three[0][0] != "fish":
    fail_tests("Does `most_common()` have the most common words from `bag_of_words`?")
  elif any([any([word == "to" for word in pair]) for pair in most_common_three]):
    fail_tests("Does `most_common()` only have the three most common words from `bag_of_words`?")
  
except NameError:
  fail_tests("Make sure to define `most_common_three`.")

pass_tests()
