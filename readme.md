A RESTful API providing JSON data containing fighter objects with a simple frontend UI.

Fighter model consists of a name, striking style and grappling style all of type string.

Available routes:

api/ - [GET] - returns the complete collection of fighter data

api/grappling/{style} - [GET] - returns the complete collection of grappling fighter data

api/striking/{style} - [GET] - returns the complete collection of striking fighter data