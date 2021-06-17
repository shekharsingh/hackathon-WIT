package com.example.connectforgood

import android.R.attr
import android.app.Activity
import android.content.Intent
import android.net.Uri
import android.os.Bundle
import android.view.View
import androidx.activity.result.contract.ActivityResultContracts
import androidx.appcompat.app.AppCompatActivity


class UploadVideo : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_upload_video)

        val chooseButton = findViewById<android.widget.Button>(R.id.buttonChoose)
        val uploadButton = findViewById<android.widget.Button>(R.id.buttonUpload)

        val textView = findViewById<android.widget.TextView>(R.id.textView)
        //val textViewResp = findViewById<android.widget.TextView>(R.id.textViewResponse)
        val progressBar = findViewById<android.widget.ProgressBar>(R.id.progressBar)

        var resultLauncher = registerForActivityResult(ActivityResultContracts.StartActivityForResult()) { result ->
            if (result.resultCode == RESULT_OK) {
                // There are no request codes
                val data: Intent? = result.data
                //doSomeOperations()

                val selectedImageUri: Uri? = data?.getData()
                val selectedPath = selectedImageUri?.path
                textView.setText(selectedPath)
            }
        }

        fun openGalleryForVideo() {
            val intent = Intent()
            intent.type = "video/*"
            intent.action = Intent.ACTION_PICK
            //TBD
            //startActivityForResult(Intent.createChooser(intent, "Select Video"),REQUEST_CODE)
            resultLauncher.launch(intent)

        }

        chooseButton.setOnClickListener {
            //val intent = Intent (this, UploadVideo::class.java)
            //startActivity(intent)
            openGalleryForVideo()
        }

        uploadButton.setOnClickListener {
            progressBar.visibility = View.VISIBLE
            UploadUtility(this).uploadFile("/Users/rimplep/AndroidStudioProjects/")
            // performing some dummy time taking operation
            /*try {
                var i=0;
                while(i<(Int.MAX_VALUE/100)){
                    i++
                }
            } catch (e: InterruptedException) {
                e.printStackTrace()
            }*/
            progressBar.visibility = View.GONE
            val intent = Intent (this, StockDetail::class.java)
            startActivity(intent)
        }

    }

}