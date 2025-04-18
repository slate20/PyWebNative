import os
import json
import sys
import time

class API:
    """
    Python backend API for the Simple Notepad application
    """
    
    def __init__(self):
        self.window = None
        self.notes_file = 'notes.json'
        
    def init(self, window):
        """Initialize the API with the window object"""
        self.window = window
        return True
    
    def get_notes(self):
        """Load saved notes from file"""
        if os.path.exists(self.notes_file):
            try:
                with open(self.notes_file, 'r') as f:
                    return json.load(f)
            except Exception as e:
                print(f"Error loading notes: {e}")
                return []
        return []
    
    def save_note(self, note):
        """Save a new note or update an existing note"""
        try:
            notes = self.get_notes()
            
            # If note has an id, update existing note
            if 'id' in note and note['id']:
                for i, existing_note in enumerate(notes):
                    if existing_note['id'] == note['id']:
                        notes[i] = note
                        break
            else:
                # Create a new note with a timestamp-based ID
                note['id'] = str(int(time.time() * 1000))
                note['created'] = time.strftime('%Y-%m-%d %H:%M:%S')
                notes.append(note)
            
            # Save to file
            with open(self.notes_file, 'w') as f:
                json.dump(notes, f, indent=2)
            
            return {'success': True, 'note': note}
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def delete_note(self, note_id):
        """Delete a note by its ID"""
        try:
            notes = self.get_notes()
            notes = [note for note in notes if note['id'] != note_id]
            
            # Save to file
            with open(self.notes_file, 'w') as f:
                json.dump(notes, f, indent=2)
            
            return {'success': True}
        except Exception as e:
            return {'success': False, 'error': str(e)}
