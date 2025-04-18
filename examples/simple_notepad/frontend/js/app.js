// Simple Notepad Application JavaScript
document.addEventListener('DOMContentLoaded', () => {
    // Wait for pywebview API to be available before initializing
    waitForPywebviewApi();
});

// Function to wait for the pywebview API to be available
function waitForPywebviewApi() {
    if (window.pywebview && window.pywebview.api) {
        // API is available, initialize the app
        initApp();
    } else {
        // API not available yet, wait and try again
        console.log('Waiting for pywebview API to be available...');
        setTimeout(waitForPywebviewApi, 100);
    }
}

// Global variables
let currentNote = null;
let allNotes = [];

async function initApp() {
    try {
        // Load notes when the app starts
        await loadNotes();
        
        // Set up event listeners
        setupEventListeners();
        
        // Initialize the editor state
        resetEditor();
    } catch (error) {
        console.error('Error initializing app:', error);
    }
}

async function loadNotes() {
    try {
        // Call the Python backend method to get notes
        allNotes = await window.pywebview.api.get_notes();
        renderNotesList();
    } catch (error) {
        console.error('Error loading notes:', error);
    }
}

function renderNotesList() {
    const notesListElement = document.getElementById('notes-list');
    
    // Clear the current list
    notesListElement.innerHTML = '';
    
    if (allNotes.length === 0) {
        notesListElement.innerHTML = '<div class="empty-state">No notes yet. Create one!</div>';
        return;
    }
    
    // Sort notes by created date (newest first)
    allNotes.sort((a, b) => {
        return new Date(b.created) - new Date(a.created);
    });
    
    // Create note items
    allNotes.forEach(note => {
        const noteElement = document.createElement('div');
        noteElement.className = 'note-item';
        if (currentNote && note.id === currentNote.id) {
            noteElement.classList.add('active');
        }
        
        // Get a preview of the content (first 30 characters)
        const contentPreview = note.content.substring(0, 30) + (note.content.length > 30 ? '...' : '');
        
        noteElement.innerHTML = `
            <h3>${note.title || 'Untitled Note'}</h3>
            <p>${contentPreview}</p>
        `;
        
        // Add click event to open the note
        noteElement.addEventListener('click', () => {
            openNote(note);
        });
        
        notesListElement.appendChild(noteElement);
    });
}

function openNote(note) {
    currentNote = note;
    
    // Update the editor
    document.getElementById('note-title').value = note.title || '';
    document.getElementById('note-content').value = note.content || '';
    
    // Update the active state in the list
    renderNotesList();
    
    // Enable the delete button
    document.getElementById('delete-note-btn').disabled = false;
}

function resetEditor() {
    currentNote = null;
    document.getElementById('note-title').value = '';
    document.getElementById('note-content').value = '';
    document.getElementById('delete-note-btn').disabled = true;
    
    // Update the active state in the list
    renderNotesList();
}

async function saveCurrentNote() {
    const titleElement = document.getElementById('note-title');
    const contentElement = document.getElementById('note-content');
    
    const title = titleElement.value.trim();
    const content = contentElement.value.trim();
    
    // Validate input
    if (!title && !content) {
        alert('Please enter a title or content for your note.');
        return;
    }
    
    // Prepare note object
    const note = {
        id: currentNote ? currentNote.id : null,
        title: title || 'Untitled Note',
        content: content,
        updated: new Date().toISOString().slice(0, 19).replace('T', ' ')
    };
    
    try {
        // Call the Python backend method to save the note
        const result = await window.pywebview.api.save_note(note);
        
        if (result.success) {
            // Update the current note with the saved version
            currentNote = result.note;
            
            // Refresh the notes list
            await loadNotes();
        } else {
            alert(`Error saving note: ${result.error}`);
        }
    } catch (error) {
        console.error('Error saving note:', error);
        alert('An error occurred while saving the note.');
    }
}

async function deleteCurrentNote() {
    if (!currentNote || !currentNote.id) {
        return;
    }
    
    if (!confirm('Are you sure you want to delete this note?')) {
        return;
    }
    
    try {
        // Call the Python backend method to delete the note
        const result = await window.pywebview.api.delete_note(currentNote.id);
        
        if (result.success) {
            // Reset the editor
            resetEditor();
            
            // Refresh the notes list
            await loadNotes();
        } else {
            alert(`Error deleting note: ${result.error}`);
        }
    } catch (error) {
        console.error('Error deleting note:', error);
        alert('An error occurred while deleting the note.');
    }
}

function setupEventListeners() {
    // New note button
    document.getElementById('new-note-btn').addEventListener('click', resetEditor);
    
    // Save note button
    document.getElementById('save-note-btn').addEventListener('click', saveCurrentNote);
    
    // Delete note button
    document.getElementById('delete-note-btn').addEventListener('click', deleteCurrentNote);
}
