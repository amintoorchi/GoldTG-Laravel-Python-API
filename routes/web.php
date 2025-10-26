<?php

use App\Http\Controllers\PriceController;
use Illuminate\Support\Facades\Route;

Route::get('/', function () {
    return response()->json([
        'message' => 'Access Denied'
    ], 403);
});

Route::post('/price/store', [PriceController::class ,'store']);
Route::get('price/show', [PriceController::class, 'show']);
