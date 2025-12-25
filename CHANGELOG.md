# Changelog

All notable changes to the Customers module will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-12-25

### Added

- Initial release of Customers module
- **Core Features**
  - Customer management (create, edit, view, deactivate)
  - Customer search and filtering
  - Customer profile with purchase history
  - Tax ID (NIF/CIF) support

- **Models**
  - `Customer`: Customer data with contact info and purchase stats

- **Views**
  - Customer list with search
  - Customer detail view
  - Customer creation form
  - Customer edit form

- **Internationalization**
  - English translations (base)
  - Spanish translations

### Technical Details

- Integration with Sales module for purchase tracking
- Integration with Invoicing module for customer data
- Soft delete (deactivate) instead of hard delete

---

## [Unreleased]

### Planned

- Customer import/export (CSV, Excel)
- Customer groups and categories
- Loyalty points system
- Customer analytics dashboard
