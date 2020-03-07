// 28. Implement strStr()
// Implement strStr().

// Return the index of the first occurrence of needle in haystack, or -1 if 
// needle is not part of haystack.

class Solution {
public:
    int strStr(string haystack, string needle)
    {
        bool done = false;
        if (needle.size() == 0)
            return 0;
        for (int i = 0; i < haystack.size(); i++)
        {
            if (haystack[i] == needle[0])
            {
                for (int j = 0; j < needle.size(); j++)
                {
                    done = true;
                    if (haystack[i + j] != needle[j])
                    {
                        done = false;
                        break;
                    }
                }
                if (done)
                    return i;
            }
        }
        return -1;
    }
};
