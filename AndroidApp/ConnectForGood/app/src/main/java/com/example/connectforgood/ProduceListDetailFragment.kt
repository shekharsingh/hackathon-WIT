package com.example.connectforgood

import android.os.Bundle
import androidx.fragment.app.Fragment
import com.google.android.material.appbar.CollapsingToolbarLayout
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import com.example.connectforgood.placeholder.PlaceholderContent
import com.example.connectforgood.databinding.FragmentProducelistDetailBinding

/**
 * A fragment representing a single ProduceList detail screen.
 * This fragment is either contained in a [ProduceListListFragment]
 * in two-pane mode (on larger screen devices) or self-contained
 * on handsets.
 */
class ProduceListDetailFragment : Fragment() {

    /**
     * The placeholder content this fragment is presenting.
     */
    private var item: PlaceholderContent.PlaceholderItem? = null

    lateinit var itemDetailTextView: TextView

    private var _binding: FragmentProducelistDetailBinding? = null

    // This property is only valid between onCreateView and
    // onDestroyView.
    private val binding get() = _binding!!

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        arguments?.let {
            if (it.containsKey(ARG_ITEM_ID)) {
                // Load the placeholder content specified by the fragment
                // arguments. In a real-world scenario, use a Loader
                // to load content from a content provider.
                item = PlaceholderContent.ITEM_MAP[it.getString(ARG_ITEM_ID)]
            }
        }
    }

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {

        _binding = FragmentProducelistDetailBinding.inflate(inflater, container, false)
        val rootView = binding.root

        binding.toolbarLayout?.title = item?.content

        itemDetailTextView = binding.producelistDetail
        // Show the placeholder content as text in a TextView.
        item?.let {
            itemDetailTextView.text = it.details
        }

        return rootView
    }

    companion object {
        /**
         * The fragment argument representing the item ID that this fragment
         * represents.
         */
        const val ARG_ITEM_ID = "item_id"
    }

    override fun onDestroyView() {
        super.onDestroyView()
        _binding = null
    }
}