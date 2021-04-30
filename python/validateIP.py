def validIPAddress(IP):
    
      def isIPv4(s):
          print(s)
          if str(int(s)) == s and 0 <= int(s) <= 255:
              return True
          return False
      def isIPv6(s):
          if len(s) > 4:
              return False
          elif int(s, 16) >= 0 and s[0] != '-':
              return True
          return False
      if IP.count(".") == 3 and all(isIPv4(i) for i in IP.split(".")):
         return "IPv4"
      if IP.count(":") == 7 and all(isIPv6(i) for i in IP.split(":")):
         return "IPv6"
      return "Neither"
print(validIPAddress("172.16.254.1"))
