# 🎨 Image Color Analyzer

A modern, responsive web application that analyzes uploaded images to extract and display their most dominant colors. Built with vanilla HTML, CSS, and JavaScript using industry-standard image processing techniques.

## ✨ Features

### Core Functionality
- **Smart Color Detection**: Analyzes images to find the most common colors
- **Real-time Processing**: Client-side analysis with no server dependency
- **Multiple Format Support**: Works with JPG, PNG, GIF, and other common image formats
- **Drag & Drop Interface**: Simply drag images onto the page or browse to select

### Data Science Standards
- **Color Quantization**: Groups similar colors to reduce noise and improve accuracy
- **Statistical Analysis**: Provides percentage breakdowns and frequency rankings
- **Performance Optimization**: Intelligent sampling for large images
- **Precision Control**: Adjustable color grouping for optimal results

### User Experience
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile
- **Interactive Elements**: Hover effects and smooth animations
- **Visual Feedback**: Loading states and progress indicators
- **Clean Results Display**: Color swatches with detailed information

## 🚀 Quick Start

### Option 1: Direct Use
1. Save the HTML file to your computer
2. Open it in any modern web browser
3. Upload an image and start analyzing!

### Option 2: Web Server
```bash
# Simple Python server
python -m http.server 8000

# Or with Node.js
npx serve .
```

Then visit `http://localhost:8000` in your browser.

## 📱 How to Use

### Step 1: Upload Your Image
- **Drag & Drop**: Simply drag an image file onto the upload area
- **Browse**: Click "Choose Image" to select from your device
- **Formats**: Supports JPG, PNG, GIF, WebP, and more

### Step 2: Wait for Analysis
- The app will automatically process your image
- Larger images may take a few seconds
- A progress indicator shows the analysis is running

### Step 3: Explore Results
- **Color Swatches**: Visual representation of dominant colors
- **Color Information**: HEX codes, RGB values, and percentages
- **Statistics**: Image dimensions, pixels analyzed, and color rankings
- **Interactive Cards**: Hover over color cards for animations

## 🔧 Technical Details

### Image Processing Algorithm

1. **Image Loading**: Canvas API loads and renders the uploaded image
2. **Scaling**: Large images are scaled down to 400px max dimension for performance
3. **Pixel Sampling**: Smart sampling reduces processing time while maintaining accuracy
4. **Color Quantization**: Similar colors are grouped using 8-bit precision reduction
5. **Frequency Analysis**: Colors are counted and ranked by occurrence
6. **Result Generation**: Top 12 colors are selected and formatted for display

### Performance Optimizations

- **Adaptive Sampling**: Automatically adjusts sample rate based on image size
- **Color Grouping**: Reduces similar colors to prevent fragmentation
- **Canvas Scaling**: Processes smaller versions of large images
- **Efficient Data Structures**: Uses Map for O(1) color lookups

### Browser Compatibility

- ✅ Chrome 60+
- ✅ Firefox 55+
- ✅ Safari 12+
- ✅ Edge 79+

## 🎯 Use Cases

### Design & Creative
- **Color Palette Extraction**: Generate color schemes from photos
- **Brand Analysis**: Analyze competitor logos and designs
- **Art Reference**: Extract colors from paintings or artwork

### Web Development
- **Theme Creation**: Build CSS color variables from images
- **Design Systems**: Create consistent color palettes
- **Asset Analysis**: Understand color distribution in designs

### Data Analysis
- **Image Statistics**: Quantify color distribution in datasets
- **Visual Research**: Analyze color trends across image collections
- **Quality Control**: Verify color consistency in product photos

## 🛠️ Customization

### Adjusting Color Sensitivity
```javascript
// In the analyzeImage function, modify this line:
const groupedR = Math.floor(r / 8) * 8; // Change 8 to adjust grouping
```

### Changing Number of Colors
```javascript
// Modify this line to show more/fewer colors:
.slice(0, 12); // Change 12 to desired number
```

### Performance Tuning
```javascript
// Adjust sampling rate:
const step = Math.max(1, Math.floor(data.length / 40000)); // Change 40000
```

## 📊 Output Format

### Color Information Provided
- **HEX Code**: #FF5733 (web-standard color code)
- **RGB Values**: Red: 255, Green: 87, Blue: 51
- **Percentage**: 23.4% (portion of image)
- **Ranking**: #1 (popularity rank)

### Statistics Displayed
- **Image Dimensions**: Original width × height
- **Pixels Analyzed**: Total number processed
- **Dominant Colors**: Count of unique colors found
- **Most Common**: Percentage of the top color

## 🔬 Algorithm Details

### Color Quantization Process
The app uses a simplified quantization method that groups colors into "buckets":

```
Original Color: RGB(127, 134, 142)
Quantized Color: RGB(120, 128, 136)
Bucket Size: 8 (adjustable)
```

This approach:
- Reduces noise from slight color variations
- Improves processing speed
- Creates more meaningful color groups
- Maintains visual accuracy

### Sampling Strategy
For large images, the algorithm samples pixels strategically:
- **Maximum Samples**: ~10,000 pixels
- **Even Distribution**: Samples across entire image
- **Skip Transparent**: Ignores pixels with low alpha
- **Adaptive Rate**: Adjusts based on image size

## 🚨 Limitations

### File Size
- Very large images (>10MB) may cause browser slowdowns
- Recommended maximum: 5MB per image

### Color Accuracy
- Quantization may group slightly different colors
- Monitor calibration affects color perception
- Lighting in source image impacts results

### Browser Memory
- Processing many large images may consume significant RAM
- Refresh page if performance degrades

## 🤝 Contributing

Want to improve the color analyzer? Here are some ideas:

### Enhancement Opportunities
- **Additional Formats**: Support for TIFF, BMP, or RAW files
- **Export Features**: Save color palettes as CSS, JSON, or Adobe swatches
- **Advanced Analysis**: Color temperature, brightness distribution
- **Batch Processing**: Analyze multiple images simultaneously

### Code Structure
```
color-analyzer.html
├── HTML Structure (markup)
├── CSS Styles (responsive design)
└── JavaScript Logic
    ├── File Handling
    ├── Image Processing
    ├── Color Analysis
    └── UI Updates
```

## 📄 License

This project is open source and available under the MIT License. Feel free to use, modify, and distribute as needed.

## 🆘 Troubleshooting

### Common Issues

**Image Won't Load**
- Check file format (JPG, PNG, GIF supported)
- Verify file isn't corrupted
- Try a smaller file size

**Analysis Takes Too Long**
- Large images require more processing time
- Try resizing image before upload
- Refresh page and try again

**Colors Look Different**
- Monitor calibration affects color display
- Different devices may show slight variations
- Colors are quantized/grouped for analysis

**Browser Compatibility**
- Update to latest browser version
- Enable JavaScript if disabled
- Clear browser cache if needed

### Getting Help
- Check browser console for error messages
- Verify image file integrity
- Test with different image formats

---

**Made with ❤️ for designers, developers, and color enthusiasts**