#!/bin/bash

# Emit the HTTP response header
echo "X-function: Emitting a hereis document"
echo "Content-type: text/html"


# Emit a blank line to separate the HTTP response header from the HTTP response body 
echo ""

USER=cg160746
# Emit the HTTP response body
cat <<EOF
<!-- Start of the Body -->
<html>
  <head>
     <title>Hello!</title>
  </head>
  <body>
    <h1>A Simple HTML Document</h1>
    "Hello!"
"X-cit-384-student: $USER"
Date: Tue, 21 Sept 2021 08:12:31 PST
From: christianne.gargoles.439@my.csun.edu
  </body>
</html>
<!-- End of the Body -->
EOF
