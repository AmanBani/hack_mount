"use client"

import { useRef } from "react"
import { Card, CardContent, CardDescription, CardHeader, CardTitle, CardFooter } from "@/components/ui/card"
import { Input } from "@/components/ui/input"
import { Button } from "@/components/ui/button"
import { Label } from "@/components/ui/label"

export default function LoginPage() {
  const emailRef = useRef<HTMLInputElement>(null)
  const passwordRef = useRef<HTMLInputElement>(null)

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()

   
    const email = emailRef.current?.value
    const password = passwordRef.current?.value

    console.log("Login attempt:", { email, password })
    
    
  }

  return (
    <div className="flex items-center justify-center min-h-screen bg-gray-100">
      <Card className="w-[450px]">
        <CardHeader>
          <CardTitle className="flex justify-center text-5xl font-extrabold text-blue-500">Login</CardTitle>
          <CardDescription className="flex  justify-center text-2xl font-bold text-black-900">Enter your Credentials.</CardDescription>
        </CardHeader>
        <form onSubmit={handleSubmit}>
          <CardContent>
            <div className="grid w-full items-center gap-4">
              <div className="flex flex-col space-y-1.5">
                <Label htmlFor="email">Email</Label>
                <Input id="email" type="email" placeholder="Your email" ref={emailRef} required />
              </div>
              <div className="flex flex-col space-y-1.5">
                <Label htmlFor="password">Password</Label>
                <Input id="password" type="password" placeholder="Your password" ref={passwordRef} required />
              </div>
            </div>
          </CardContent>
          <CardFooter>
            <Button type="submit" className="w-full">
              Login
            </Button>
          </CardFooter>
        </form>
      </Card>
    </div>
  )
}

