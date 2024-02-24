import {useEffect, useState} from 'react'
import './App.css'
import ContactList from "./ContactList.jsx";
import ContactForm from "./ContactForm.jsx";

function App() {
    const[contacts,setContacts] = useState([])
    const [isModalOpen,setIsModalOpen] = useState(false)

    useEffect(()=>{
        fetchContacts()
    },[])

    const fetchContacts = async () =>{
        const response = await fetch("http://127.0.0.1:5000/contacts")
        const data = await response.json()
        setContacts(data.contacts)
        console.log(data.contacts)
    }

    const  closeModal = ()=>{
        setIsModalOpen(false)
    }

    const openCreateModal =()=>{
        if(!isModalOpen) setIsModalOpen(true)
    }

   return (<>
      <ContactList contacts={contacts}/>
      <ContactForm />
      </>)
}
export default App


