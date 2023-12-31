{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "1213251a",
   "metadata": {},
   "source": [
    "# 1.Create a null vector of size 10 but the fifth value which is 1."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "45bb3590",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0. 0. 0. 0. 1. 0. 0. 0. 0. 0.]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "\n",
    "n = np.zeros(10)\n",
    "n[4] = 1\n",
    "print(n)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e6f96f0f",
   "metadata": {},
   "source": [
    "# 2. Create a vector with values ranging from 10 to 49."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "910924a7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,\n",
       "       27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43,\n",
       "       44, 45, 46, 47, 48, 49])"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "n = np.arange(10,50)\n",
    "n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0a96338f",
   "metadata": {},
   "source": [
    "# 3. Create a 3x3 matrix with values ranging from 0 to 8"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "6d43ad21",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[0, 1, 2],\n",
       "       [3, 4, 5],\n",
       "       [6, 7, 8]])"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "n = np.arange(0,9)\n",
    "matrix = n.reshape(3,3)\n",
    "matrix"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fe1c0434",
   "metadata": {},
   "source": [
    "# 4. Find indices of non-zero elements from [1,2,0,0,4,0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "cdb3fe63",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(array([0, 1, 4], dtype=int64),)"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "n = [1,2,0,0,4,0]\n",
    "a = np.array(n)\n",
    "i = np.where(a != 0)\n",
    "i\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ab85eb23",
   "metadata": {},
   "source": [
    "# 5.Create a 10x10 array with random values and find the minimum and maximum values."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "42b989f6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "max values is :  0.982852487716025\n",
      "min values is :  0.0011971890587495482\n"
     ]
    }
   ],
   "source": [
    "ran = np.random.rand(10,10)\n",
    "print(\"max values is : \", np.max(ran))\n",
    "print(\"min values is : \", np.min(ran))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a9037307",
   "metadata": {},
   "source": [
    "# 6. Create a random vector of size 30 and find the mean value."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "c4a9e419",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[148 181 144 176 185 182 154 167 150 108 193 152 120 130 133 180 169 164\n",
      " 139 170 148 124 150 180 164 112 180 174 142 190]\n",
      "mean value is :  156.96666666666667\n"
     ]
    }
   ],
   "source": [
    "n = np.random.randint(100,200,30)\n",
    "print(n)\n",
    "m = np.mean(n)\n",
    "print(\"mean value is : \",m)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
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
   "version": "3.11.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}