# Django Tree Menu App

A Django app for creating and managing tree-structured menus with support for multiple menus on a single page.

## Features

- Create and manage hierarchical menus using the Django admin interface
- Render menu using a custom template tag
- Automatically set active menu items based on the current page's URL
- Support for named URLs and custom URLs for menu items
- Efficient database query - only 1 query per menu

## Installation

1. Clone the repository or download the project files
2. Create a virtual environment for the project:

  ```
  python -m venv venv
  ```

3. Activate the virtual environment:

- On Linux or macOS:

  ```
  source venv/bin/activate
  ```

- On Windows:

  ```
  venv\Scripts\activate
  ```

4. Install the requirements:

  ```
  pip install -r requirements.txt
  ```

5. Run `python manage.py migrate` to apply the database migrations

## Usage

1. Import the custom template tag in your template file:

```html
{% load menu_tags %}
```
2. Use the draw_menu tag to render a menu by name:

```html
{% draw_menu 'main_menu' %}
```
3. Add and manage menu items using the Django admin interface

## File Structure

  * models.py: Contains the MenuItem model, which represents a menu item and its properties.
  * admin.py: Registers the MenuItem model in the Django admin interface using MPTTModelAdmin.
  * menu_tags.py: Contains the custom template tag draw_menu that renders the menu in the template.
  * menu.html: The template file that renders the menu structure with the active menu items and submenus.

