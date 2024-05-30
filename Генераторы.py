def all_variants(s):
    if not s:
        yield ''
    else:
        for variant in all_variants(s[1:]):
            yield variant
            yield s[0] + variant


a = all_variants("abc")
for i in a:
 print(i)