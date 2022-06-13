def tag(t):
    t2 = t
    t2 = t[0] + '/' + t[1:]

    def title(str):
        return t + str.title() + t2
    return title

t =tag('<h4>')
p = t('python class')
print(p)
