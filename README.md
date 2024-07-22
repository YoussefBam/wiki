# wiki
## Features
### Entry Page 
Visiting /wiki/TITLE, where TITLE is the title of an encyclopedia entry, should render a page that displays the contents of that encyclopedia entry : 
If an entry is requested that does not exist, the user should be presented with an error page indicating that their requested page was not found.
If the entry does exist, the user should be presented with a page that displays the content of the entry. The title of the page should include the name of the entry.

### Search
Allow the user to type a query into the search box in the sidebar to search for an encyclopedia entry :
If the query matches the name of an encyclopedia entry, the user should be redirected to that entry’s page.
If the query does not match the name of an encyclopedia entry, the user should instead be taken to a search results page that displays a list of all encyclopedia entries that have the query as a substring.

### Create New Page
create a new encyclopedia entry : 
When the page is saved, if an encyclopedia entry already exists with the provided title, the user should be presented with an error message.
Otherwise, the encyclopedia entry should be saved to disk, and the user should be taken to the new entry’s page.

### Edit Page 
On each entry page, the user should be able to click a link to be taken to a page where the user can edit that entry’s Markdown content :
Once the entry is saved, the user should be redirected back to that entry’s page.

### Random Page 
Clicking “Random Page” in the sidebar should take user to a random encyclopedia entry.

## stack used 
Django
Pyhton
HTML
CSS
Markdown files.

# Acknowledgements
The CSS, the util functions, the layout, few lines of index page and the file structure were done by CS50. The implimentations above are my work
