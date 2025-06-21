{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "6ee708a7-a500-48b4-a8b1-54bbbb213426",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\t\t\tWELCOME TO GRADE CALCULATOR\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter marks for subject 1: 40\n",
      "Enter marks for subject 2: 40\n",
      "Enter marks for subject 3: 40\n",
      "Enter marks for subject 4: 40\n",
      "Enter marks for subject 5: 40\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "40.0\n",
      "You have scored D\n"
     ]
    }
   ],
   "source": [
    "print(\"\\t\\t\\tWELCOME TO GRADE CALCULATOR\")\n",
    "marks1=float(input(\"Enter marks for subject 1:\"))\n",
    "marks2=float(input(\"Enter marks for subject 2:\"))\n",
    "marks3=float(input(\"Enter marks for subject 3:\"))\n",
    "marks4=float(input(\"Enter marks for subject 4:\"))\n",
    "marks5=float(input(\"Enter marks for subject 5:\"))\n",
    "total=marks1+marks2+marks3+marks4+marks5\n",
    "percentage=(total/500)*100\n",
    "print(\"Total percentage:\",percentage)\n",
    "if percentage>=90:\n",
    "    print(\"You have got A\")\n",
    "elif percentage>=70:\n",
    "    print(\"You have scored B\")\n",
    "elif percentage>=60:\n",
    "    print(\"You have scored C\")\n",
    "elif percentage>=40:\n",
    "    print(\"You have scored D\")\n",
    "elif percentage<=39:\n",
    "    print(\"You have scored F\")\n",
    "else:\n",
    "    print(\"Invalid\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "243e5d4f-5204-4c58-a67b-f91a70466308",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
