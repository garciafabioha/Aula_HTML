"use client"

import { createCar } from "../actions/create-car"
import { Button } from "./button"

export const AddForm = () => {
    return (
        <form action={createCar}>
            <label className="block border border-gray-500 p-4 mb-3">
                <input type="file" name="img" accept="image/*" required/>
            </label>
            <label className="block border border-gray-500 p-4 mb-3">
                <input type="text" name="title" placeholder="Digite o modelo do carro"
                className="bg-black text-white text-lg w-full outline-none" required/>
            </label>    
            <label className="block border border-gray-500 p-4 mb-3">
                <input type="number" name="price_from" placeholder="Preço Inicial"
                className="bg-black text-white text-lg w-full outline-none" required/>
            </label> 
            <label className="block border border-gray-500 p-4 mb-3">
                <input type="number" name="price_to" placeholder="Preço Atual"
                className="bg-black text-white text-lg w-full outline-none" required/>
            </label> 
            <label className="block border border-gray-500 p-4 mb-3">
                <input type="checkbox" name="negotiable"/> Negociável?
            </label>  
            <label className="block border border-gray-500 p-4 mb-3">
                <input type="text" name="author_name" placeholder="Digite o nome do vendedor"
                className="bg-black text-white text-lg w-full outline-none" required/>
            </label>              
            <label className="block border border-gray-500 p-4 mb-3">
                <input type="email" name="author_email" placeholder="Digite o email do vendedor"
                className="bg-black text-white text-lg w-full outline-none" required/>
            </label>    
            <label className="block border border-gray-500 p-4 mb-3">
                <textarea name="description" rows={4}
                 className="resize-none bg-black text-white text-lg w-full outline-none"/>
            </label> 
            <Button label="Cadastrar"/>
        </form>
    )    
}