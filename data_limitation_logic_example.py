from sqlalchemy import create_engine, MetaData, Table, delete, select
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta

# Assuming you have SQLAlchemy engine and session set up
engine = create_engine('postgresql://username:password@localhost:5432/ecommerce_db')
Session = sessionmaker(bind=engine)
session = Session()

# Example: Function to enforce data retention policy
def enforce_data_retention(max_storage_bytes):
    # Query to check current storage usage (simplified example)
    total_storage_used = session.execute("SELECT pg_database_size('ecommerce_db');").scalar()

    if total_storage_used > max_storage_bytes:
        # Determine how much data to delete (oldest records first)
        records_to_delete = session.query(Order).order_by(Order.created_at).limit(100).all()

        # Delete the oldest records
        for record in records_to_delete:
            session.delete(record)
        
        session.commit()
        print(f"Deleted {len(records_to_delete)} records to free up space.")

# Example usage: Enforce data retention policy if storage exceeds 1 GB (for demonstration)
max_storage_bytes = 1073741824  # 1 GB in bytes
enforce_data_retention(max_storage_bytes)
