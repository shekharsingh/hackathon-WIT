package com.example.connectforgood

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val sellButton = findViewById<android.widget.Button>(R.id.sellButton)
        val buyButton = findViewById<android.widget.Button>(R.id.buyButton)

        sellButton.setOnClickListener {
            val intent = Intent (this, UploadVideo::class.java)
            startActivity(intent)

        }

        buyButton.setOnClickListener {
            val intent = Intent (this, ProduceListDetailHostActivity::class.java)
            startActivity(intent)

        }
    }
}