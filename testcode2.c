void tokenize(const char* source_code) {
    char word[100]; // Comment
    int word_idx = 0;
    int line_number = 1;

    for (const char* p = source_code; *p; p++) {
        if (*p == '\n') {
            line_number++;
        }

        if (*p == ' ' || *p == '\t' || *p == '\n') {
            if (word_idx > 0) {
                word[word_idx] = '\0'; // test
// test
                if (is_keyword(word)) {
                    printf("Keyword: %s (Line: %d)\n", word, line_number);
                } else {
                    printf("Identifier: %s (Line: %d)\n", word, line_number);
                }

                word_idx = 0;
            }
        } else if (is_operator(*p)) {
            printf("Operator: %c (Line: %d)\n", *p, line_number);
        } else {
            word[word_idx++] = *p;
        }
    }
}