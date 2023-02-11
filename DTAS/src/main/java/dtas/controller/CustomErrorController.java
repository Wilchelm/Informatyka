package dtas.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.autoconfigure.web.ErrorAttributes;
import org.springframework.boot.autoconfigure.web.ErrorController;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.context.request.RequestAttributes;
import org.springframework.web.context.request.ServletRequestAttributes;

import javax.persistence.EntityExistsException;
import javax.persistence.EntityNotFoundException;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.util.HashMap;
import java.util.Map;

/**
 * @author Arkadiusz Rosiak (http://www.rosiak.it)
 * @date 2016-10-13
 */
@ControllerAdvice
@RestController
public class CustomErrorController implements ErrorController {

    private static final String PATH = "/error";

    @Autowired
    private ErrorAttributes errorAttributes;

    private ResponseEntity error(int status, String message){
        Map<String, Object> respBody = new HashMap<>();
        respBody.put("status", status);
        respBody.put("message", message);

        return ResponseEntity.status(status).body(respBody);
    }

    @RequestMapping(value = PATH)
    ResponseEntity catchError(HttpServletRequest request, HttpServletResponse response) {
        return error(response.getStatus(), getErrorAttributes(request, false).get("error").toString());
    }

    @ExceptionHandler(value = EntityNotFoundException.class)
    public ResponseEntity handleEntityNotFoundException(Exception e){
        return error(404, e.getMessage());
    }

    @ExceptionHandler(value = EntityExistsException.class)
    public ResponseEntity handleEntityExistsException(Exception e){
        return error(409, e.getMessage());
    }

    @ExceptionHandler(value = Exception.class)
    public ResponseEntity handleException(Exception e){
        return error(500, e.getMessage());
    }

    @Override
    public String getErrorPath() {
        return PATH;
    }

    private Map<String, Object> getErrorAttributes(HttpServletRequest request, boolean includeStackTrace) {
        RequestAttributes requestAttributes = new ServletRequestAttributes(request);
        return errorAttributes.getErrorAttributes(requestAttributes, includeStackTrace);
    }

}