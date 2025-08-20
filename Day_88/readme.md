# ☕ WorkCafe - Remote Work Cafe Finder

A modern web application that helps remote workers and digital nomads find the perfect cafe for productive work sessions.

## 🚧 Project Status: In Development

This project is currently **ongoing** and in active development. The frontend is complete and functional with sample data, but the backend API integration is still in progress.

## ✨ Current Features

- **Modern, responsive design** that works on all devices
- **Real-time search** - Find cafes by name or location
- **Smart filtering** - Filter by WiFi strength, power outlets, quiet spaces
- **Detailed cafe cards** showing:
  - Star ratings and review counts
  - Available amenities (WiFi, power, quiet space, coffee quality)
  - Operating hours
  - Location information
- **Interactive UI** with smooth animations and hover effects

## 🛠️ Tech Stack

### Frontend (Complete)
- **HTML5** - Semantic structure
- **CSS3** - Modern styling with gradients, animations, and responsive design
- **JavaScript** - Interactive functionality and data filtering

### Backend (Planned)
- **SQLite** - Database for cafe management
- **API endpoints** for:
  - Searching cafes
  - Adding new cafes
  - Deleting cafes
  - Updating cafe information

## 🎯 Upcoming Features

- [ ] **Backend API** integration with SQLite database
- [ ] **CRUD operations** for cafe management (Create, Read, Update, Delete)
- [ ] **Database schema** for cafes, amenities, and ratings
- [ ] **Admin panel** for adding/editing cafes
- [ ] **User reviews** and rating system
- [ ] **Map integration** for cafe locations
- [ ] **Favorite cafes** functionality
- [ ] **Advanced filters** (price range, seating capacity, etc.)

## 🗄️ Database Schema (Planned)

The SQLite database will include tables for:

```sql
-- Cafes table
CREATE TABLE cafes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    address TEXT NOT NULL,
    rating REAL DEFAULT 0.0,
    hours TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Amenities table
CREATE TABLE amenities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cafe_id INTEGER,
    amenity_type TEXT NOT NULL,
    FOREIGN KEY (cafe_id) REFERENCES cafes (id)
);

-- Reviews table (future feature)
CREATE TABLE reviews (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cafe_id INTEGER,
    rating INTEGER,
    comment TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (cafe_id) REFERENCES cafes (id)
);
```

## 🚀 Getting Started

### Current Version (Frontend Only)

1. Clone this repository
2. Open `index.html` in your web browser
3. Explore the sample cafes and test the search/filter functionality

### Future Version (With Backend)

Once the API is complete:

1. Clone the repository
2. Install dependencies (TBD)
3. Set up the SQLite database
4. Start the API server
5. Open the frontend

## 📱 How to Use

1. **Search**: Use the search bar to find cafes by name or location
2. **Filter**: Click filter buttons to show only cafes with specific amenities:
   - "Strong WiFi" - Cafes with reliable internet
   - "Power Outlets" - Cafes with charging stations
   - "Quiet Space" - Cafes suitable for focused work
3. **Browse**: Scroll through cafe cards to find your perfect workspace

## 🎨 Design Philosophy

The design focuses on:
- **Clarity** - Easy to scan information at a glance
- **Modern aesthetics** - Gradient backgrounds and smooth animations
- **Mobile-first** - Responsive design that works on all screen sizes
- **User experience** - Intuitive navigation and helpful visual cues

## 🤝 Contributing

This project is still in development. Once the API is complete, contributions will be welcome for:
- Adding new cafe data
- Improving the user interface
- Adding new features
- Bug fixes and optimizations

## 📄 License

[License information to be added]

## 📧 Contact

[Contact information to be added]

---

**Note**: This is a work-in-progress project. The current version displays sample data for demonstration purposes. The full functionality with database integration is coming soon!