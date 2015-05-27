__author__ = 'effy'
'''
Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
'''

class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        a = path.split("/")
        st = []
        for i in a:
            if i == "..":
                if st:
                    st.pop()
            elif i == ".":
                pass
            elif i:
                st.append(i)
        if not st:
            return "/"

        return '/'+'/'.join(st)


class Solution_secondround:
    # @param {string} path
    # @return {string}
    def simplifyPath(self, path):
        dirs = path.split('/')
        simple = []
        for i in dirs:
            if i =='..':
                if simple:
                    simple.pop()
            elif i == '.' or i == '':
                pass
            else:
                simple.append(i)
        if not simple:
            return '/'
        return '/' + '/'.join(simple)



a = Solution()
print a.simplifyPath("/a/./b/../../c/")


