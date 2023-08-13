def getSpamEmails(subjects, spam_words):
    # Write your code here
    result = []

    spam_set = set([s.lower() for s in spam_words])
    for subject in subjects:
        spam_count = 0
        for word in subject.split():
            if word.lower() in spam_set:
                spam_count += 1
        if spam_count > 1:
            result.append("spam")
        else:
            result.append("not_spam")
    return result
