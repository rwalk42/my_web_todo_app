import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("Band Setlist Sharing App")
st.subheader("This allows us to share the setlist and running order online...")
st.write("Add suggestions to the end of the list. Check the box to remove a song")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()


st.text_input(label="Enter a Song and Artist (separated by a dash)", placeholder="Add new song - artist....",
              on_change=add_todo, key='new_todo')





#st.session_state