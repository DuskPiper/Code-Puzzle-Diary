class Solution():
    def findNthDigit(self, n):
        n -= 1
        for layer in range(1, 11):#layer是考察的位数，从1位数开始考察，考察结束则（最后一行）扣除当前位数所有digit总数，余量作剩余考察。终止于11是考虑到输入的n的大小限定
            new_base = 10**(layer - 1)#当前考察位数的最小数，比如考察3位数则是100
            if n < 9 * new_base * layer:#当前考察layer所占有的digit数量，如果n（原n扣除之前位数所占digit后的余量）比这个小，则说明答案就是当前位数（return），否则就考察更高一位数（扣除当前位数并继续循环）
                return int(str(new_base + n/layer)[n%layer])#当前位最小数+n（余量）除以数的位数的整数部分就是目标数字（我们不关心小数部分），取其数字的第[n%layer]位为答案
            n -= 9 * new_base * layer#扣除当前位数的所有digit数量，将余量用作考察更高一位数