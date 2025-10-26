<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Price;

class PriceController extends Controller
{
    public function store(Request $request)
    {
        $validated = $request->validate([
            'price' => 'required',
        ]);

        $price = Price::create($validated);

        return response()->json([
            'message' => 'Price saved successfully!',
            'price' => $price
        ], 201);
    }

    public function show(){
        return response()->json(Price::latest()->get());
    }


}
