#!/bin/bash
#Emit a blank line to separate the HTTP response header from the HTTP response body

USERNAME=${QUERY_STRING#*username=}
USERNAME=${USERNAME%%&*}
USERNAME=${USERNAME//+/ }

#header
echo "Content-Type:text/html" 
#blank line
echo ""

#Emit the HTTP response body 
cat << EOF
<!--Start of the Body -->
<html>
<head>
<title>Name List </title>
</head>
<body>
"You entered this Username:" $USERNAME
</body>
</html>
<!--End of the Body -->
EOF
