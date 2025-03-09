import json
import os
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
engine = create_engine(f'sqlite:///{os.path.join(BASE_DIR, "cities.db")}')
Session = sessionmaker(bind=engine)
Base = declarative_base()

class City(Base):
    __tablename__ = 'cities'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    country = Column(String(100), nullable=False)
    population = Column(Integer)
    latitude = Column(Float)
    longitude = Column(Float)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'country': self.country,
            'population': self.population,
            'latitude': self.latitude,
            'longitude': self.longitude
        }

def init_db():
    Base.metadata.create_all(engine)
    session = Session()
    if session.query(City).count() == 0:
        with open(os.path.join(BASE_DIR, 'cities.json'), 'r') as f:
            cities_data = json.load(f)
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
    session = Session()
    query = session.query(City)
    if search_term:
        query = query.filter(City.name.ilike(f'%{search_term}%'))
    cities = [city.to_dict() for city in query.all()]
    session.close()
    return cities

def get_countries(search_query=None):
    session = Session()
    query = session.query(City.country).distinct()
    if search_query:
        query = query.filter(City.country.ilike(f'%{search_query}%'))
    countries = [country for country, in query.all()]
    session.close()
    return countries 