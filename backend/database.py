import json
import os
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create SQLite database
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
engine = create_engine(f'sqlite:///{os.path.join(BASE_DIR, "cities.db")}')
Session = sessionmaker(bind=engine)
Base = declarative_base()

class City(Base):
    """City model for database"""
    __tablename__ = 'cities'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    country = Column(String(100), nullable=False)
    population = Column(Integer)
    latitude = Column(Float)
    longitude = Column(Float)
    
    def to_dict(self):
        """Convert city object to dictionary"""
        return {
            'id': self.id,
            'name': self.name,
            'country': self.country,
            'population': self.population,
            'latitude': self.latitude,
            'longitude': self.longitude
        }

def init_db():
    """Initialize database and load sample data"""
    Base.metadata.create_all(engine)
    
    # Check if we already have data
    session = Session()
    if session.query(City).count() == 0:
        # Load sample data from JSON file
        with open(os.path.join(BASE_DIR, 'cities.json'), 'r') as f:
            cities_data = json.load(f)
        
        # Add cities to database
        for city_data in cities_data:
            city = City(
                id=city_data['id'],
                name=city_data['name'],
                country=city_data['country'],
                population=city_data['population'],
                latitude=city_data['latitude'],
                longitude=city_data['longitude']
            )
            session.add(city)
        
        session.commit()
    
    session.close()

def get_cities(search_term=None):
    """Get cities from database, optionally filtered by search term"""
    session = Session()
    query = session.query(City)
    
    if search_term:
        query = query.filter(City.name.ilike(f'%{search_term}%'))
    
    cities = [city.to_dict() for city in query.all()]
    session.close()
    return cities

def get_city_by_id(city_id):
    """Get a specific city by ID"""
    session = Session()
    city = session.query(City).filter(City.id == city_id).first()
    result = city.to_dict() if city else None
    session.close()
    return result